import React from "react";
import { useNavigate } from "react-router-dom"
import useToken from "@galvanize-inc/jwtdown-for-react";



function Account() {


  const navigate = useNavigate()
  const { logout } = useToken()
  const handleLogout = () => {
    logout()
    navigate("/")
  }

  const { token } = useToken();

  return (
    <div className="account">
      <div className="card">
        <div className="card-body">
          <h5 className="card-title">Account</h5>
          <div>
            <div>
              {!token && (
                <button
                  className="button success"
                  onClick={() => navigate("/signup")}
                >
                  Sign Up
                </button>
              )}
              {!token && (
                <button
                  className="button primary"
                  onClick={() => navigate("/login")}
                >
                  Login
                </button>
              )}
            </div>

            {token && <button className="button danger" onClick={handleLogout}>
              Logout
            </button>}
          </div>
        </div>
      </div>
    </div>
  );
}

export default Account;
