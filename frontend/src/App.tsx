import { useState } from 'react';
import axios from 'axios';
import { SubmitCodeForm } from './components/SubmitCodeForm/SubmitCodeForm';

function App() {
  const [code, setCode] = useState('');
  const [review, setReview] = useState('');
  const [loading, setLoading] = useState(false);

  const handleSubmit = async () => {
    setLoading(true);
    try {
      const response = await axios.post('http://localhost:8000/review', { code });
      setReview(response.data.review);
    } catch (error) {
      setReview('Error fetching review.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="p-4 bg-gray-100 px-8">
      <h1 className="text-3xl font-bold mb-6 text-center ">AI Code Reviewer</h1>
      <SubmitCodeForm handleSubmit={handleSubmit} loading={loading} />


      {review && (
        <div className="w-full max-w-2xl mt-6 bg-white p-4 rounded shadow-md">
          <h2 className="font-semibold text-lg mb-2">Review Output:</h2>
        </div>
      )}
    </div>
  );
}

export default App;