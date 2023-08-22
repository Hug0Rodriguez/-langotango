// import React, { useState, useEffect } from "react";
// import "./Chat.css";
// const SpeechRecognition =
//   window.SpeechRecognition || window.webkitSpeechRecognition;
// const mic = new SpeechRecognition();

// mic.continuous = true;
// mic.interimResults = true;
// mic.lang = ("en-US", "es-ES", "gr-DE", "vi-VN");

// function Chat() {
//   const [isListening, setIsListening] = useState(false);
//   const [audio, setAudio] = useState(null);
//   const [savedAudio, setSavedAudio] = useState([]);

//   useEffect(() => {
//     handleListen();
//   }, [isListening]);

//   const handleStop = async (event) => {
//     event.preventDefault();
//     setIsListening(false);
//     const data = {};
//     data.saved_audio = savedAudio;
//     data.created_at = Date.now();
//     const chatUrl = "http://localhost:8000/api/messages/";
//     const fetchOptions = {
//       method: "post",
//       body: JSON.stringify(data),
//       headers: {
//         "Content-Type": "application/json",
//       },
//     };

//     const audioResponse = await fetch(chatUrl, fetchOptions);
//     if (audioResponse.ok) {
//       setSavedAudio("");
//     } else {
//       console.log(`audioResponse error: ${JSON.stringify(audioResponse)}`);
//     }
//   };

//   const handleListen = () => {
//     if (isListening) {
//       mic.start();
//       mic.onend = () => {
//         console.log("continue..");
//         mic.start();
//       };
//     } else {
//       mic.stop();
//       mic.onend = () => {
//         console.log("Stopped Mic on Click");
//       };
//     }
//     mic.onstart = () => {
//       console.log("Mics on");
//     };

//     mic.onresult = (event) => {
//       const transcript = Array.from(event.results)
//         .map((result) => result[0])
//         .map((result) => result.transcript)
//         .join("");
//       console.log(transcript);
//       setAudio(transcript);
//       mic.onerror = (event) => {
//         console.log(event.error);
//       };
//     };
//   };

//   const handleStart = () => {
//     setIsListening(true);
//   };

//   const handleSaveNote = () => {
//     setSavedAudio([...savedAudio, audio]);
//     setAudio("");
//   };

//   return (
//     <>
//       <h1>Chat</h1>
//       <div className="container">
//         <div className="box">
//           <h2>Current Chat</h2>
//           {isListening ? <span>🎙️</span> : <span>🛑🎙️</span>}
//           <button onClick={handleSaveNote} disabled={!audio}>
//             Save Chat
//           </button>
//           <button onClick={handleStart} disabled={isListening}>
//             Start
//           </button>
//           <button onClick={handleStop} disabled={!isListening}>
//             Stop
//           </button>
//           <p>{audio}</p>
//         </div>
//         <div className="box">
//           <h2>Chat</h2>
//           {savedAudio.map((n) => (
//             <p key={n}>{n}</p>
//           ))}
//         </div>
//       </div>
//     </>
//   );
// }

// export default Chat;


// import React, { useState, useEffect } from "react";

// const SpeechRecognition =
//   window.SpeechRecognition || window.webkitSpeechRecognition;
// const mic = new SpeechRecognition();

// mic.continuous = true;
// mic.interimResults = true;

// function Chat() {
//   const [isListening, setIsListening] = useState(false);
//   const [audio, setAudio] = useState("");
//   const [savedAudio, setSavedAudio] = useState([]);
//   const [selectedLanguage, setSelectedLanguage] = useState("en-US"); // Default language

//   useEffect(() => {
//     handleListen();
//     // eslint-disable-next-line
//   }, [isListening, selectedLanguage]);

//   const handleListen = () => {
//     mic.lang = selectedLanguage;

//     if (isListening) {
//       mic.start();
//       mic.onend = () => {
//         mic.start();
//       };
//     } else {
//       mic.stop();
//       mic.onend = () => {
//         console.log("Stopped Mic on Click");
//       };
//     }

//     mic.onstart = () => {
//       console.log("Mics on");
//     };

//     mic.onresult = (event) => {
//       const transcript = Array.from(event.results)
//         .map((result) => result[0])
//         .map((result) => result.transcript)
//         .join("");
//       setAudio(transcript);
//       mic.onerror = (event) => {
//         console.log(event.error);
//       };
//     };
//   };

//   const handleSaveNote = () => {
//     setSavedAudio([...savedAudio, audio]);
//     setAudio("");
//   };

//   const handleLanguageChange = (language) => {
//     setSelectedLanguage(language);
//     setIsListening(false); // Stop listening when language changes
//   };

//   return (
//     <>
//       <h1>Chat</h1>
//       <div className="container">
//         <div className="box">
//           <h2>Current Chat</h2>
//           {isListening ? <span>🎙️</span> : <span>🛑🎙️</span>}
//           <button onClick={handleSaveNote} disabled={!audio}>
//             Save Chat
//           </button>
//           <button onClick={() => setIsListening((prevState) => !prevState)}>
//             Start/Stop
//           </button>
//           <select
//             value={selectedLanguage}
//             onChange={(e) => handleLanguageChange(e.target.value)}
//           >
//             <option value="en-US">English (US)</option>
//             <option value="es-ES">Spanish (Spain)</option>
//             <option value="de-DE">German (Germany)</option>
//             <option value="vi-VN">Vietnamese (Vietnam)</option>
//           </select>
//           <p>{audio}</p>
//         </div>
//         <div className="box">
//           <h2>Chat History</h2>
//           {savedAudio.map((n, index) => (
//             <p key={index}>{n}</p>
//           ))}
//         </div>
//       </div>
//     </>
//   );
// }

// export default Chat;


import React, { useState, useEffect } from "react";


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

  useEffect(() => {
    handleListen();
  }, [isListening, selectedLanguage]);

  const handleStop = async (event) => {
    event.preventDefault();
    setIsListening(false);
  //   const data = {};
  //   data.text = savedAudio;
  //   data.created_at = Date.now();
  //   const chatUrl = "http://localhost:8000/api/messages/";
  //   const fetchOptions = {
  //     method: "post",
  //     body: JSON.stringify(data),
  //     headers: {
  //       "Content-Type": "application/json",
  //     },
  //   };

  //   const audioResponse = await fetch(chatUrl, fetchOptions);
  //   if (audioResponse.ok) {
  //     setSavedAudio("");
  //   } else {
  //     console.log(`audioResponse error: ${JSON.stringify(audioResponse)}`);
  //   }
  };

  const handleListen = () => {
    console.log(isListening)
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
      console.log(event.results)
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
          </select>
          <p>{audio}</p>
        </div>
        <div className="box">
          <h2>Chat</h2>
          {savedAudio.map((n) => (
            <p key={n}>{n}</p>
          ))}
        </div>
      </div>
    </>
  );
}

export default Chat;
