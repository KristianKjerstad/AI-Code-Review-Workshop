import { useState } from 'react';
import axios from 'axios';
import { UserInput } from './components/form/UserInput';


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
      <UserInput />

      <button
        onClick={handleSubmit}
        className="px-6 py-2 bg-blue-600 text-white font-semibold rounded shadow hover:bg-blue-700 transition-colors"
        disabled={loading}
      >
        {loading ? 'Reviewing...' : 'Submit for Review'}
      </button>

      {review && (
        <div className="w-full max-w-2xl mt-6 bg-white p-4 rounded shadow-md">
          <h2 className="font-semibold text-lg mb-2">Review Output:</h2>
        </div>
      )}
    </div>
  );
}

export default App;