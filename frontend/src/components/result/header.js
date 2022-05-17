import React from 'react';

const ResultHeader = () => {
    return (
        <div className="row mx-md-4 justify-content-around">

            <h3 className="display-4">Genie Prep</h3>

            <div className="row">
                <div className="col">
                    <span className="lead mb-0">Practise result</span>
                </div>

                <div className="col text-end">
                    <span className="mb-0">Date: <strong> 12/05/2022</strong></span>
                </div>
            </div>

        </div>
    );
};

export default ResultHeader;