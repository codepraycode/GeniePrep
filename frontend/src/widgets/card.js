import React from 'react';

const Card = ({extraclass, children}) => {
    return (
        <div className={`${extraclass || ''} card`}>
            {children}
        </div>
    );
};

export default Card;