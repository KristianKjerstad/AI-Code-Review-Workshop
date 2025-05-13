type MessageBubbleProps = {
    variant: 'user' | 'reviewer'
    output: string;
}

export function MessageBubble({variant, output}: MessageBubbleProps) {
    let classes;
    if(variant === 'user') {
        classes = "bg-[#467865] min-h-60 w-100 p-2 text-white rounded shadow-md flex justify-end";
    }
    if(variant === 'reviewer') {
        classes = "bg-[#46786533] min-h-60 min-w-100 p-2 text-black rounded shadow-md";
    }

    return (
        <div className={classes}>
            <p className="flex justify-start">
                {output}
            </p>
        </div>
    )
}