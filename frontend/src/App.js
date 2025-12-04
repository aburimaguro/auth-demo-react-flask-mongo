import React, { useEffect, useState } from "react";
import Signup from "./pages/Signup";
import Login from "./pages/Login";
import Profile from "./pages/Profile";
import { refresh } from "./api";
import "./styles.css";

export default function App() {
  const [accessToken, setAccessToken] = useState(null);
  const [page, setPage] = useState("login");

  useEffect(() => {
    (async () => {
      try {
        const data = await refresh();
        if (data && data.access_token) {
          setAccessToken(data.access_token);
          setPage("profile");
        }
      } catch (err) {
        // ignore
      }
    })();
  }, []);

  return (
    <div className="container">
      <header>
        <h1>Auth Demo</h1>
        <nav>
          <button onClick={() => setPage("login")}>Login</button>
          <button onClick={() => setPage("signup")}>Signup</button>
          <button onClick={() => setPage("profile")}>Profile</button>
        </nav>
      </header>

      <main>
        {page === "signup" && <Signup onRegistered={(token) => { setAccessToken(token); setPage("profile"); }} />}
        {page === "login" && <Login onLoggedIn={(token) => { setAccessToken(token); setPage("profile"); }} />}
        {page === "profile" && <Profile accessToken={accessToken} onRequireLogin={() => setPage("login")} />}
      </main>
    </div>
  );
}

