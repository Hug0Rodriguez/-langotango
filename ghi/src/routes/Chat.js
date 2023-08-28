import React, { useState, useEffect } from "react";
import  { useSpeechSynthesis } from 'react-speech-kit'

const SpeechRecognition =
  window.SpeechRecognition || window.webkitSpeechRecognition;
const mic = new SpeechRecognition();

mic.continuous = true;
mic.interimResults = true;

function Chat() {
  const [isListening, setIsListening] = useState(false);
  const [audio, setAudio] = useState(null);
  const [savedAudio, setSavedAudio] = useState([]);
  const [selectedLanguage, setSelectedLanguage] = useState("en-US"); // Default language
  const [responseChat, setResponseChat] = useState();
  const {speak} = useSpeechSynthesis();

  useEffect(() => {
    handleListen();
    // eslint-disable-next-line
  }, [isListening, selectedLanguage]);

  const handleStop = async (event) => {
    event.preventDefault();
    setIsListening(false);
    const data = {};
    data.text = audio;
    console.log("🚀 ~ file: Chat.js:31 ~ handleStop ~ data:", data);
    // data.created_at = Date.now();
    const chatUrl = "http://localhost:8000/api/messages";
    const fetchOptions = {
      method: "post",
      body: JSON.stringify(data),
      headers: {
        "Content-Type": "application/json",
      },
    };
    const response = await fetch(chatUrl, fetchOptions);
    if (response.ok) {
      console.log(response.body);
      const responseData = await response.json();
      setResponseChat(responseData.text);
      setSavedAudio("");
    } else {
      console.log(`audioResponse error: ${JSON.stringify(response)}`);
    }
  };

  const handleListen = () => {
    mic.lang = selectedLanguage;

    if (isListening) {
      mic.start();
      mic.onend = () => {
        console.log("continue..");
        mic.start();
      };
    } else {
      mic.stop();
      mic.onend = () => {
        console.log("Stopped Mic on Click");
      };
    }
    mic.onstart = () => {
      console.log("Mics on");
    };

    mic.onresult = (event) => {
      const transcript = Array.from(event.results)
        .map((result) => result[0])
        .map((result) => result.transcript)
        .join("");
      console.log(transcript);
      setAudio(transcript);
      mic.onerror = (event) => {
        console.log(event.error);
      };
    };
  };

  const handleStart = () => {
    setIsListening(true);
  };

  const handleSaveNote = () => {
    setSavedAudio([...savedAudio, audio]);
    setAudio("");
  };

  const handleLanguageChange = (language) => {
    setSelectedLanguage(language);
    setIsListening(false); // Stop listening when language changes
  };


  return (
    <>
      <h1>Chat</h1>
      <div className="container">
        <div className="box">
          <h2>Current Chat</h2>
          {isListening ? <span>🎙️</span> : <span>🛑🎙️</span>}
          <button onClick={handleSaveNote} disabled={!audio}>
            Save Chat
          </button>
          <button onClick={handleStart} disabled={isListening}>
            Start
          </button>
          <button onClick={handleStop} disabled={!isListening}>
            Stop
          </button>
          <select
            value={selectedLanguage}
            onChange={(e) => handleLanguageChange(e.target.value)}
          >
            <option value="en-US">English (US)</option>
            <option value="es-ES">Spanish (Spain)</option>
            <option value="de-DE">German (Germany)</option>
            <option value="vi-VN">Vietnamese (Vietnam)</option>
            <option value="zh-Hans">Chinese (PRC)</option>
          </select>
          <p>{audio}</p>
          {responseChat && <p className="response">{responseChat}</p>}{" "}
          {audio && <p className="audio">{audio}</p>}{" "}
          {/* Display response */}
        </div>
        <div className="box">
          <h2>Chat</h2>
          {savedAudio && savedAudio.map((n) => <p key={n}>{n}</p>)}
        </div>
        <div></div>
      </div>
    </>
  );
}

export default Chat;

// import React, { useState, useEffect } from "react";

// function TextToSpeechChat() {
//   const [text, setText] = useState("");
//   const [audioSrc, setAudioSrc] = useState(null);
//   const [socket, setSocket] = useState(null);
//   useEffect(() => {
//     const ws = new WebSocket("ws://localhost:8000/ws");
//     ws.onopen = () => console.log("Connected to the WebSocket");
//     ws.onmessage = (event) => {
//       const audioBase64 = event.data;
//       setAudioSrc(`data:audio/mp3;base64,${audioBase64}`);
//     };
//     setSocket(ws);
//     return () => ws.close();
//   }, []);
//   const handleTextChange = (e) => {
//     setText(e.target.value);
//   };
//   const handleSendClick = () => {
//     if (socket) socket.send(text);
//     setText(""); // Clear the text input after sending
//   };
//   return (
//     <div>
//       <textarea value={text} onChange={handleTextChange}></textarea>
//       <button onClick={handleSendClick}>Send</button>
//       {audioSrc && (
//         <audio controls autoPlay>
//           <source src={audioSrc} type="audio/mp3" />
//           Your browser does not support the audio element.
//         </audio>
//       )}
//     </div>
//   );
// }
// export default TextToSpeechChat;
