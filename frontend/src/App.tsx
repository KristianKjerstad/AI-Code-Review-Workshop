import { useState } from 'react';
import axios from 'axios';
import { Prism as SyntaxHighlighter } from 'react-syntax-highlighter';
import { oneDark } from 'react-syntax-highlighter/dist/esm/styles/prism';
import Markdown from "react-markdown";

function App() {
  const [diff, setDiff] = useState('');
  const [intent, setIntent] = useState('');
  const [review, setReview] = useState('');
  const [loading, setLoading] = useState(false);

  const handleSubmit = async () => {
    setLoading(true);
    try {
      const response = await axios.postForm('http://localhost:5173/api/code-review', { diff, intent });
      setReview(response.data.review);
    } catch (error) {
      setReview('Error fetching review.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="p-4 bg-zinc-100 dark:bg-zinc-900 px-8 h-full">
      <img className="w-32 h-auto" src="/image.jpeg" />

      <textarea
        className="w-full max-w-2xl h-64 p-3 border border-zinc-300 rounded shadow-sm focus:outline-none focus:ring focus:border-blue-300 mb-4"
        value={diff}
        minLength={10}
        onChange={(e) => setDiff(e.target.value)}
        placeholder="Paste your diff here..."
      />

      <textarea
        className="w-full max-w-2xl h-64 p-3 border border-zinc-300 rounded shadow-sm focus:outline-none focus:ring focus:border-blue-300 mb-4"
        value={intent}
        minLength={10}
        onChange={(e) => setIntent(e.target.value)}
        placeholder="Describe your diff here..."
      ></textarea>

      <button
        onClick={handleSubmit}
        className="px-6 py-2 bg-blue-600 text-white font-semibold rounded shadow hover:bg-blue-700 transition-colors"
        disabled={loading}
      >
        {loading ? 'Reviewing...' : 'Submit for Review'}
      </button>

      {review && (
        <div className="w-full max-w-2xl mt-6 bg-white dark:bg-zinc-800 p-4 rounded shadow-md">
          <h2 className="font-semibold text-lg mb-2">Review Output:</h2>
          <Markdown>
            {review}
          </Markdown>
        </div>
      )}
    </div>
  );
}

export default App;