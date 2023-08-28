import React from "react";
// import { useState } from "react";
// import useToken from "@galvanize-inc/jwtdown-for-react";


function Account({ isLoggedIn, handleLogin, handleLogout, handleSignUp }) {
  return (
    <div className="account">
      <div className="card">
        <div className="card-body">
          <h5 className="card-title">Account</h5>
          <div>
            {!isLoggedIn && (
              <div>
                <button className="button success" onClick={handleSignUp}>
                  Sign Up
                </button>
                <button className="button primary" onClick={handleLogin}>
                  Login
                </button>
              </div>
            )}
            {isLoggedIn && (
              <button className="button danger" onClick={handleLogout}>
                Logout
              </button>
            )}
          </div>
          {!isLoggedIn && (
            <div>

            </div>
          )}
        </div>
      </div>
    </div>
  );
}

export default Account;
