import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { setToken } from '../lib/api';

export default function Login() {
  const [email, setEmail] = useState('admin@acme.com');
  const [password, setPassword] = useState('securepassword123');
  const navigate = useNavigate();

  const handleLogin = async (e: React.FormEvent) => {
    e.preventDefault();
    const formData = new URLSearchParams();
    formData.append('username', email);
    formData.append('password', password);

    try {
      const res = await fetch('http://localhost:8000/api/v1/auth/login', {
        method: 'POST',
        headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
        body: formData.toString(),
      });
      const data = await res.json();
      if (res.ok) {
        setToken(data.access_token);
        navigate('/');
      } else {
        alert('Login failed: ' + data.detail);
      }
    } catch (err) {
      alert('Network error');
    }
  };

  return (
    <div style={{ maxWidth: 400, margin: '100px auto', fontFamily: 'sans-serif' }}>
      <h2>DataSentinel Pro Login</h2>
      <form onSubmit={handleLogin} style={{ display: 'flex', flexDirection: 'column', gap: 10 }}>
        <input value={email} onChange={e => setEmail(e.target.value)} placeholder="Email" style={{ padding: 8 }} />
        <input type="password" value={password} onChange={e => setPassword(e.target.value)} placeholder="Password" style={{ padding: 8 }} />
        <button type="submit" style={{ padding: 10, background: '#007bff', color: 'white', border: 'none', cursor: 'pointer' }}>Login</button>
      </form>
    </div>
  );
}