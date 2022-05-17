import React from 'react';

const Button = ({type, text, classes}) => {
    return (
        <button type={type || 'button'} className={`${classes || ''} btn`}>
            {text}
        </button>
    );
};

export default Button;