import React from 'react';

const Question = () => {
    return (
        <>

            <div class="labels">
                <p>Question 01</p>

                <p>Index</p>
            </div>

            <div className="options">
                <div className="option_item card selected">
                    This is an Option
                </div>

                <div className="option_item card">
                    This is an Option
                </div>

                <div className="option_item card">
                    This is an Option
                </div>

                <div className="option_item card">
                    This is an Option
                </div>
            </div>

            
        </>
    );
};

export default Question;