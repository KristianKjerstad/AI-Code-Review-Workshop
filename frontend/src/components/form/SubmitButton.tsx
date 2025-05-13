type SubmitButtonProps = {
    handleSubmit: () => Promise<void>;
    loading: boolean;
};
  

export function SubmitButton({handleSubmit, loading}: SubmitButtonProps) {
    return (
        <button
            onClick={handleSubmit}
            className="px-6 py-2 bg-blue-600 text-white font-semibold rounded shadow hover:bg-blue-700 transition-colors"
            disabled={loading}
        >
            {loading ? 'Reviewing...' : 'Submit code'}
        </button>)
}