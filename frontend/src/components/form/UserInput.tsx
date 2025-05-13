export function UserInput() {
    return (
        <div className="flex flex-col my-2">
            <textarea name="user-input" id="user-input" placeholder="Write your code" className="p-1 h-[200px] w-max-[700px] border-1 rounded-md" />
        </div>
    )
}