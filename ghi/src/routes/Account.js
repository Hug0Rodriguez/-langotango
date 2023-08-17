import React from "react";

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
              <div className="input-container">
                <label htmlFor="name" className="input-label">
                  Name
                </label>
                <input type="text" className="input" id="name" />
              </div>
              <div className="input-container">
                <label htmlFor="email" className="input-label">
                  Username
                </label>
                <input type="email" className="input" id="email" />
              </div>
              <div className="input-container">
                <label htmlFor="password" className="input-label">
                  Password
                </label>
                <input type="password" className="input" id="password" />
              </div>
            </div>
          )}
        </div>
      </div>
    </div>
  );
}

export default Account;
