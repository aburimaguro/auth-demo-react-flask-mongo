import React, { useState } from "react";
import { register } from "../api";

export default function Signup({ onRegistered }) {
  const [email, setEmail] = useState("");
  const [name, setName] = useState("");
  const [password, setPassword] = useState("");
  const [msg, setMsg] = useState(null);

  async function submit(e) {
    e.preventDefault();
    setMsg("Registering...");
    const data = await register({ email, password, name });
    if (data && data.access_token) {
      setMsg("Registered.");
      onRegistered(data.access_token);
    } else {
      setMsg((data && data.error) || "Registration failed");
    }
  }

  return (
    <div>
      <h2>Sign up</h2>
	<div className="form-container">
	  <form onSubmit={submit}>
        <label>Email<input value={email} onChange={e => setEmail(e.target.value)} /></label><br/>
        <label>Name<input value={name} onChange={e => setName(e.target.value)} /></label><br/>
        <label>Password<input type="password" value={password} onChange={e => setPassword(e.target.value)} /></label><br/>
        <button type="submit">Register</button>
      </form>

	</div>
            {msg && <p>{msg}</p>}
    </div>
  );
}

