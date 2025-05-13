type SubmitButtonProps = {
    handleSubmit: () => Promise<void>;
    loading: boolean;
};
  

export function SubmitButton({handleSubmit, loading}: SubmitButtonProps) {
    return (
        <button
            onClick={handleSubmit}
            className="px-6 py-2 bg-[#467865] text-white font-semibold rounded shadow hover:bg-[#2b4a3e] hover:cursor-pointer transition-colors w-full"
            disabled={loading}
        >
            {loading ? 'Reviewing...' : 'Submit code'}
        </button>)
}