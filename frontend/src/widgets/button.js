import React from 'react';

const Button = ({type, text, classes, ...rest}) => {
    return (
        <button type={type || 'button'} className={`${classes || ''} btn`} {...rest}>
            {text}
        </button>
    );
};

export default Button;