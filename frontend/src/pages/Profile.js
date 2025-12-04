import React, { useEffect, useState } from "react";
import { getProfile, logout, refresh } from "../api";

export default function Profile({ accessToken, onRequireLogin }) {
  const [user, setUser] = useState(null);

  async function fetchProfile(token) {
    if (!token) { setUser(null); return; }
    const data = await getProfile(token);
    if (data && data.user) {
      setUser(data.user);
    } else if (data && data.error === "unauthorized") {
      const ref = await refresh();
      if (ref && ref.access_token) {
        const newData = await getProfile(ref.access_token);
        if (newData && newData.user) setUser(newData.user);
        else { setUser(null); onRequireLogin(); }
      } else { onRequireLogin(); }
    } else { onRequireLogin(); }
  }

  useEffect(() => { fetchProfile(accessToken); }, [accessToken]);

  async function doLogout() {
    await logout();
    setUser(null);
    onRequireLogin();
  }

  if (!user) return <div><p>Not logged in.</p></div>;

  return (
    <div className="profile-info">
      <h2>Profile</h2>
      <p><strong>Email:</strong> {user.email}</p>
      <p><strong>Name:</strong> {user.name || "-"}</p>
      <button className="logout-btn" onClick={doLogout}>Logout</button>
    </div>
  );
}

