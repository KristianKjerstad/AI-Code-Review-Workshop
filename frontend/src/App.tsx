import { useState } from 'react';
import axios from 'axios';
import { SubmitCodeForm } from './components/SubmitCodeForm/SubmitCodeForm';
import { MessageBubble } from './components/MessageBubble/MessageBubble';

function App() {
  const [code, setCode] = useState("");
  
  const [review, setReview] = useState("");
  const [showReview, setShowReview] = useState(false);
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
    <div className=" bg-white m-auto px-8 h-screen flex flex-col justify-between max-w-[800px]">
      <div className="flex justify-center mt-10">
        <div className="flex flex-col">
          <h1 className="text-2xl font-bold text-center text-gray-800 uppercase text-left">
            Koala code
          </h1>
          <h2 className="text-3xl font-bold text-center text-gray-800 mt-0 uppercase text-left logo-color">
            reviewer
          </h2>
        </div>
        <div className="flex justify-center ml-2 mb-10">
          <img
            src="../src/assets/koalaLogo.png"
            alt="Koala Code logo"
            className="w-15 h-auto"
          />
        </div>
      </div>
      {showReview && (
          <MessageBubble variant='user' output={code} />
      )}

      <div className='flex flex-col items-center pb-18'>
        {!showReview && (
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
