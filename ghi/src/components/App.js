import { useEffect, useState } from "react";
import Construct from "./Construct.js";
import ErrorNotification from "./ErrorNotification";
import { AuthProvider } from "@galvanize-inc/jwtdown-for-react";
import "./App.css";

function App() {
  const [launchInfo, setLaunchInfo] = useState([]);
  const [error, setError] = useState(null);
  const baseUrl = "http://localhost:3000";

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
    <AuthProvider baseUrl={baseUrl}>
    <div>
      <ErrorNotification error={error} />
      <Construct info={launchInfo} />
    </div>
    </AuthProvider>
    </>
  );
}

export default App;
