import { useEffect, useState } from 'react';
import { useQuery } from '@tanstack/react-query';
import { BarChart, Bar, XAxis, YAxis, Tooltip, ResponsiveContainer } from 'recharts';
import { fetchApi, removeToken } from '../lib/api';
import { useNavigate } from 'react-router-dom';

export default function Dashboard() {
  const [wsMessage, setWsMessage] = useState<string>('Connecting to stream...');
  const navigate = useNavigate();

  // React Query to fetch data sources
  const { data: sources, isLoading, error } = useQuery({
    queryKey: ['sources'],
    queryFn: () => fetchApi('/data-sources/'),
  });

  // WebSocket connection
  useEffect(() => {
    const ws = new WebSocket('ws://localhost:8000/ws/');
    ws.onopen = () => setWsMessage('Connected. Waiting for events...');
    ws.onmessage = (event) => setWsMessage(event.data);
    
    return () => {
      ws.onclose = null; // Prevent React strict mode false warnings
      ws.close();
    };
  }, []);

  const handleLogout = () => {
    removeToken();
    navigate('/login');
  };

  const chartData = [
    { name: 'Mon', ingested: 4000 },
    { name: 'Tue', ingested: 3000 },
    { name: 'Wed', ingested: 2000 },
    { name: 'Thu', ingested: 2780 },
    { name: 'Fri', ingested: 1890 },
  ];

  if (isLoading) return <div style={{ padding: 20 }}>Loading dashboard...</div>;
  if (error) return <div style={{ padding: 20, color: 'red' }}>Error: {error.message}</div>;

  return (
    <div style={{ padding: 20, fontFamily: 'sans-serif' }}>
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
        <h1>DataSentinel Pro Dashboard</h1>
        <button onClick={handleLogout} style={{ padding: '8px 16px', cursor: 'pointer' }}>Logout</button>
      </div>
      
      <div style={{ padding: 15, background: '#f0f0f0', borderRadius: 5, marginBottom: 20 }}>
        <strong>Real-time Event Stream:</strong> <code>{wsMessage}</code>
      </div>

      <div style={{ display: 'flex', gap: 20 }}>
        <div style={{ flex: 1, border: '1px solid #ccc', padding: 15, borderRadius: 5 }}>
          <h3>Data Sources</h3>
          <ul>
            {sources?.map((source: any) => (
              <li key={source.id}>
                <strong>{source.name}</strong> ({source.source_type}) - {source.status}
              </li>
            ))}
          </ul>
        </div>

        <div style={{ flex: 1, border: '1px solid #ccc', padding: 15, borderRadius: 5, height: 300 }}>
          <h3>Data Ingestion Volume</h3>
          <ResponsiveContainer width="100%" height="100%">
            <BarChart data={chartData}>
              <XAxis dataKey="name" />
              <YAxis />
              <Tooltip />
              <Bar dataKey="ingested" fill="#8884d8" />
            </BarChart>
          </ResponsiveContainer>
        </div>
      </div>
    </div>
  );
}