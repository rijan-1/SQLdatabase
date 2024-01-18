import React, { useContext, useEffect, useState } from "react";

import {Register} from "./components/Register";


import { UserContext } from "UserContext";

const App = () => {
  const [message, setMessage] = useState("");
  const [token] = useContext(UserContext);

  const getWelcomeMessage = async () => {
    const requestOptions = {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
      },
    };
    const response = await fetch("/api", requestOptions);
    const data = await response.json();

    if (!response.ok) {
      console.log("something messed up");
    } else {
      setMessage(data.message);
    }
  };

  useEffect(() => {
    getWelcomeMessage();
  }, []);

  return (
    <>

      <div className="columns">
        <div className="column"></div>
        <div className="column m-5 is-two-thirds">
          {!token &&(
            <div className="columns">
              <Register /> 
            </div>
          ) 
           
          }
        </div>
        <div className="column"></div>
      </div>
    </>
  );
};

export default App;