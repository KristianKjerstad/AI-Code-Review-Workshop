import { UserInput } from '../form/UserInput';
import { SubmitButton } from '../form/SubmitButton';

type SubmitCodeForm = {
    handleSubmit: () => Promise<void>;
    loading: boolean;
};

export function SubmitCodeForm({handleSubmit, loading}: SubmitCodeForm) {
    return (
        <div>
             <UserInput />
             <SubmitButton handleSubmit={handleSubmit} loading={loading} />
        </div>
    )
}