import { useState } from 'react';
import axios from 'axios';
import { SubmitCodeForm } from './components/SubmitCodeForm/SubmitCodeForm';

function App() {
  const [code, setCode] = useState("");
  const [review, setReview] = useState("");
  const [loading, setLoading] = useState(false);

  const handleSubmit = async () => {
    setLoading(true);
    try {
      const response = await axios.post("http://localhost:8000/review", {
        code,
      });
      setReview(response.data.review);
    } catch (error) {
      setReview("Error fetching review.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="p-4 bg-white px-8 h-screen flex flex-col justify-between">
      <div className="flex justify-center mt-10">
        <h1 className="text-xl font-bold text-center text-gray-800 mt-10">
          Koala code
        </h1>
        <h2 className="text-xl font-bold text-center text-gray-800 mt-10 ml-1">
          reviewer
        </h2>
        <div className="flex justify-center ml-2 mb-10">
          <img
            src="../src/assets/koalaLogo.png"
            alt="Koala Code logo"
            className="w-12 h-auto"
          />
        </div>
      </div>
      {review && (
        <div className="w-full max-w-2xl mt-6 bg-white p-4 rounded shadow-md">
          <h2 className="font-semibold text-lg mb-2">Review Output:</h2>
        </div>
      )}

      <div className='flex flex-col items-center pb-18'>
        {!review && (
          <div className='text-center'>
            <p>
              If you feed me your code, 
            </p>
            <p>
              I'll give you feedback.
            </p>
          </div>
        )}
      </div>



      <div className="px-8 flex flex-col">
        <SubmitCodeForm handleSubmit={handleSubmit} loading={loading} />
      </div>
    </div>
  );
}

export default App;
