import React, { useState } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [message, setMessage] = useState('');
  const [response, setResponse] = useState('');
  const [error, setError] = useState('');
  const [isLoading, setIsLoading] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setIsLoading(true);
    setError('');

    try {
      const result = await axios.post('http://localhost:8000/api/chat/', {
        message: message
      });
      setResponse(result.data.response);
    } catch (err) {
      setError(err.response?.data?.error || 'An error occurred');
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-gradient-to-b from-blue-50 to-white py-6 flex flex-col justify-center sm:py-12">
      <div className="relative py-3 sm:max-w-2xl sm:mx-auto w-full px-4">
        <div className="relative px-4 py-10 bg-white shadow-2xl rounded-3xl sm:p-10 border border-blue-50">
          <div className="max-w-md mx-auto">
            <div className="space-y-6">
              <div className="text-center">
                <h1 className="text-4xl font-bold text-gray-900 mb-2">
                  AmazeBot Chat
                </h1>
                <p className="text-gray-500 text-sm">
                  Your AI assistant for amazing conversations
                </p>
              </div>

              <form onSubmit={handleSubmit} className="space-y-4">
                <div className="relative">
                  <textarea
                    value={message}
                    onChange={(e) => setMessage(e.target.value)}
                    placeholder="Type your message here..."
                    rows="4"
                    className="w-full px-4 py-3 border border-gray-200 rounded-xl focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent transition duration-200 ease-in-out text-gray-700 text-lg"
                  />
                </div>
                <button
                  type="submit"
                  disabled={isLoading}
                  className={`w-full flex items-center justify-center py-3 px-6 rounded-xl text-base font-medium transition duration-200 ease-in-out transform hover:scale-[1.02]
                    ${isLoading
                      ? 'bg-gray-300 cursor-not-allowed'
                      : 'bg-gradient-to-r from-blue-600 to-blue-700 hover:from-blue-700 hover:to-blue-800 text-white shadow-lg hover:shadow-xl'
                    }`}
                >
                  {isLoading ? (
                    <>
                      <svg className="animate-spin -ml-1 mr-3 h-5 w-5 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                        <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4"></circle>
                        <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
                      </svg>
                      Processing...
                    </>
                  ) : 'Send Message'}
                </button>
              </form>

              {error && (
                <div className="animate-fade-in mt-4 p-4 bg-red-50 border border-red-200 rounded-xl">
                  <p className="text-red-600 font-medium">{error}</p>
                </div>
              )}

              {response && (
                <div className="animate-fade-in mt-6 space-y-3">
                  <h3 className="text-lg font-semibold text-gray-900">
                    Response:
                  </h3>
                  <div className="bg-blue-50 p-5 rounded-xl border border-blue-100">
                    <p className="text-gray-700 text-lg leading-relaxed">
                      {response}
                    </p>
                  </div>
                </div>
              )}
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;
