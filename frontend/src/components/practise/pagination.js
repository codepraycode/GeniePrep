import React from 'react';

const Pagination = () => {
    return (
        <>

           <ul>
                   {[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18].map((each,i)=>{
                       return <li key={i}>{each}</li>
                   })}
               </ul>

            
        </>
    );
};

export default Pagination;