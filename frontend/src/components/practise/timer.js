import React,{useState, useEffect} from 'react';

const Timer = () => {
    const [time, setTime] = useState({
        minutes: 3,
        seconds: 0
    });

    useEffect(()=>{
        let timeInterval = setInterval(()=>{
            let {minutes, seconds} = time;

            if(seconds > 0){
                setTime((prev_time)=>{
                    prev_time.seconds -= 1

                    return {...prev_time}
                });
            }

            else if(seconds === 0){
                if(minutes === 0){
                    clearInterval(timeInterval)
                }else{
                    setTime((prev_time)=>{
                        return{
                            minutes:prev_time.minutes-1,
                            seconds:59
                        }
                    });
                }
            }
        }, 1000);


        return ()=>{
            clearInterval(timeInterval);
        }
    })

    return (
        <>
            <p className="timer">
                { time.minutes }:
                { time.seconds < 10 ? 
                    `0${ time.seconds }` 
                    : 
                    time.seconds }
            </p>
        </>
    );
};

export default Timer;