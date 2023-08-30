import { useEffect, useState } from "react";
import Construct from "./Construct.js";
import ErrorNotification from "/app/src/ErrorNotification";
import { AuthProvider } from "@galvanize-inc/jwtdown-for-react";
import "./App.css";
import {
  BrowserRouter,
  Outlet,
  Route,
  Routes,
} from "react-router-dom";
import Home from "./routes/Home";
import Accounts from "./routes/Account";
import Chat from "./routes/Chat";
import Navbar from "./components/Navbar";
import SignupForm from "./routes/Signup";
import LoginForm from "./routes/Login";
import chatHistory from "./routes/ChatHist";

function App() {
  const [launchInfo, setLaunchInfo] = useState([]);
  const [error, setError] = useState(null);
  const baseUrl = process.env.REACT_APP_API_HOST;

  useEffect(() => {
    async function getData() {
      let url = `${process.env.REACT_APP_API_HOST}/api/launch-details`;
      console.log("fastapi url: ", url);
      let response = await fetch(url);
      console.log("------- hello? -------");
      let data = await response.json();

      if (response.ok) {
        console.log("got launch data!");
        setLaunchInfo(data.launch_details);
      } else {
        console.log("drat! something happened");
        setError(data.message);
      }
    }
    getData();
  }, []);

  return (
    <>
        <div>
          <ErrorNotification error={error} />
          <BrowserRouter>
            <AuthProvider baseUrl={baseUrl}>
              <Navbar />
                <Outlet />
                  <Routes>
                    <Route path="/" element={<Home />} />
                    <Route path="/chat" element={<Chat />} />
                    <Route path="/accounts" element={<Accounts />} />
                    <Route path="/signup" element={<SignupForm />} />
                    <Route path="/login" element={<LoginForm />} />
                    <Route path="/chatHist" element={<chatHistory />} />

                </Routes>
            </AuthProvider>
          </BrowserRouter>
          <Construct info={launchInfo} />
        </div>

    </>
  );
}

export default App;
