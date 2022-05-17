import React,{useState} from 'react';

import SetUp from '../components/practise/course_setup';
import Start from '../components/practise/start';

const Test = () => {
    // const {id} = useParams();
    const [status, setStatus] = useState({
        setup:false,
        started:false

    });

    const updateStatus = (data)=>{
        setStatus((prev)=>{
            return {
                ...prev,
                ...data
            }
        });
    };


    const renderSetup = ()=>{
        let template;


        if(!status.setup){
            template = <SetUp updateStatus={updateStatus}/>
        }

        else{
            template = <Start updateStatus={updateStatus}/>
        }

        return template;
    }

    return (
        <>
            {
                !status.started ?
                    renderSetup()
                :
                <p>Starting Practice....</p>
            }
        </>
    );
}

export default Test;