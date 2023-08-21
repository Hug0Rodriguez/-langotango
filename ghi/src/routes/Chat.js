import React, { useState, useEffect } from "react";

const SpeechRecognition =
  window.SpeechRecognition || window.webkitSpeechRecognition;
const mic = new SpeechRecognition();

mic.continuous = true;
mic.interimResults = true;
mic.lang = ("en-US", "es-ES", "gr-DE", "vi-VN", "zh-ZH");

function Chat() {
  const [isListening, setIsListening] = useState(false);
  const [audio, setAudio] = useState(null);
  const [savedAudio, setSavedAudio] = useState([]);

  useEffect(() => {
    handleListen();
  }, [isListening]);

  const handleListen = () => {
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

  const handleSaveNote = () => {
    setSavedAudio([...savedAudio, audio]);
    setAudio("");
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
          <button onClick={() => setIsListening((prevState) => !prevState)}>
            Start/Stop
          </button>
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
