import React from 'react';
import Card from '../../widgets/card';
import Button from '../../widgets/button';

const Start = ({updateStatus}) => {
    return (
         <div className="practise_setup_container">

            <div className="intro">
                <h3 className="display-4">Genie Prep</h3>
                <p className="lead mb-0">
                    Practise Instruction
                </p>
            </div>

            <Card extraclass={"setup_card "}>

                <div>
                    <p class="text-muted">
                        Please read the following instructions carefully
                    </p>
                </div>


                <div className="instructions" >
                    <ol class="rounded-list">
                        <li>Every question has it match with the answers on this app
                        </li>
                        <li>Please get a hard copy of FUTA PUTME past question for your subjects with you before you begin
                        </li>
                        <li> Make sure you select the right option to the question.
                        </li>
                        <li> Do not Refresh, if you try submitting and nothing happens, wait and make sure you have an active internet connection.
                        </li>

                        <li>Press the start button below to begin, Good Luck.
                        </li>
                    </ol>
                </div>

                <hr/>


                <div>
            
                    <table 
                        className="table table-borderless" 
                    >

                        <tbody>
                            <tr>
                                <td><strong>Course</strong></td>
                                <td colSpan="">Course 001</td>
                            </tr>
                            <tr>
                                <td><strong>Number Of Questions</strong></td>
                                
                                <td colSpan="2">10</td>
                            </tr>
                            <tr>
                                <td><strong>Duration</strong></td>
                                <td colSpan="3">10 mins</td>
                            </tr>
                            
                        </tbody>
                    </table>

                </div>

                <div className="text-center buttons">

                    <Button 
                        text="Back" 
                        classes={"mr-3"} 
                        onClick={()=>{
                            updateStatus({
                                setup:false,
                                started:false
                            })
                        }}
                    />

                    <Button 
                        text="Start Pratice" 
                        classes="active"
                        onClick={()=>{
                            updateStatus({
                                started:true
                            })
                        }}
                    />

                </div>

                

            </Card>
        </div>
    );
};

export default Start;