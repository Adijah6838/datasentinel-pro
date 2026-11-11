import { render, screen } from '@testing-library/react';
import { BrowserRouter } from 'react-router-dom';
import { QueryClient, QueryClientProvider } from '@tanstack/react-query';
import Login from '../pages/Login';
import { describe, it, expect } from 'vitest';

const queryClient = new QueryClient();

describe('Login Component', () => {
  it('renders the login form correctly', () => {
    render(
      <QueryClientProvider client={queryClient}>
        <BrowserRouter>
          <Login />
        </BrowserRouter>
      </QueryClientProvider>
    );

    expect(screen.getByText('DataSentinel Pro Login')).toBeInTheDocument();
    expect(screen.getByPlaceholderText('Email')).toBeInTheDocument();
    expect(screen.getByPlaceholderText('Password')).toBeInTheDocument();
    expect(screen.getByRole('button', { name: /login/i })).toBeInTheDocument();
  });
});