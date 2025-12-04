const API_BASE = "http://localhost:5000/api";

export async function register({ email, password, name }) {
  const res = await fetch(`${API_BASE}/register`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    credentials: "include",
    body: JSON.stringify({ email, password, name })
  });
  return res.json();
}

export async function login({ email, password }) {
  const res = await fetch(`${API_BASE}/login`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    credentials: "include",
    body: JSON.stringify({ email, password })
  });
  return res.json();
}

export async function refresh() {
  const res = await fetch(`${API_BASE}/refresh`, {
    method: "POST",
    credentials: "include"
  });
  return res.json();
}

export async function logout() {
  const res = await fetch(`${API_BASE}/logout`, {
    method: "POST",
    credentials: "include"
  });
  return res.json();
}

export async function getProfile(accessToken) {
  const res = await fetch(`${API_BASE}/me`, {
    method: "GET",
    headers: { Authorization: `Bearer ${accessToken}` },
    credentials: "include"
  });
  return res.json();
}
