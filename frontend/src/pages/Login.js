import React, { useState } from "react";
import { login } from "../api";

export default function Login({ onLoggedIn }) {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [msg, setMsg] = useState(null);

  async function submit(e) {
    e.preventDefault();
    setMsg("Logging in...");
    const data = await login({ email, password });
    if (data && data.access_token) {
      setMsg("Logged in.");
      onLoggedIn(data.access_token);
    } else {
      setMsg((data && data.error) || "Login failed");
    }
  }

  return (
    <div>
      <h2>Login</h2>
      <div className="form-container">
	<form onSubmit={submit}>
        <label>Email<input value={email} onChange={e => setEmail(e.target.value)} /></label><br/>
        <label>Password<input type="password" value={password} onChange={e => setPassword(e.target.value)} /></label><br/>
        <button type="submit">Login</button>
      </form>

      </div>
            {msg && <p>{msg}</p>}
    </div>
  );
}

