import React from 'react';
import Card from '../../widgets/card';
import Button from '../../widgets/button';
import {Form} from '../../widgets/Form';

const SetUp = ({updateStatus}) => {
    return (
         <div className="practise_setup_container">
            <div className="intro">
                <h3 className="display-4">Genie Prep</h3>
                <p className="lead mb-0">Exam Setup
                (Mode <strong>practise</strong>)</p>
            </div>

            <Card extraclass={"setup_card"}>

                <div className="selectors">
                    <h5 className="text-muted ">Set Question Number range</h5>

                    
                    <div>
                        <div className="row row-cols-2">
                            <div className="col-12 col-sm-6">
                                <div className="input-group">
                                    <div className="input-group-text">From</div>
                                    <input 
                                        type="number" 
                                        min={1}
                                        max={999}
                                        className="form-control" 
                                        name="_from" 
                                        placeholder="set from"
                                    />
                                </div>
                            </div>

                            <div className="col-12 col-sm-6">
                                <div className="input-group">
                                    <div className="input-group-text">To</div>
                                    <input 
                                        type="number" 
                                        min={1}
                                        max={999}
                                        className="form-control" 
                                        name="_from" 
                                        placeholder="set stop"
                                    />
                                </div>
                            </div>
                        </div>
                    </div>
                    

                </div>


                <div className="selectors">
                    <h5 className="text-muted ">Set Time</h5>

                    <div className="timer">
                        <div className="input-group">
                            
                            <input 
                                type="number" 
                                min={20}
                                max={360}
                                className="form-control" 
                                name="_from" 
                                placeholder="set minutes"
                            />
                            <div className="input-group-text">min</div>
                        </div>
                    </div>

                </div>

                <Button text="Continue" classes="active" onClick={()=>{
                    updateStatus({
                        setup:true
                    })
                }}/>

            </Card>
        </div>
    );
};

export default SetUp;