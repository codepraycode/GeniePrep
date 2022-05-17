// Input Supporting Radio, CheckBox

import React from 'react'

const supported = ['radio', 'checkBox']

const Selection = (props) => {

    const {type, inputHandler, name, options, wrapperprops, ...rest} = props;

    // console.log(props)

    let template;

    if(!supported.includes(type)){
        template = <input type="text" placeholder="-----" readOnly />
    }


    template = options.map((option,i)=>{
            return(
                <label htmlFor={`${name}_option`} key={i}>
                    <input type={type} name={name} id={`${name}_option`}  onChange={inputHandler}/>

                    <span>{option}</span>
                </label>
            )
        }
    
    )


    // const addWrapper = (template)=>{
    //     if(wrapperprops){
    //         return (<div {...wrapperprops}>
    //             {template}
    //         </div>)
    //     }

    //     return template
    // }

    return (
        <div {...wrapperprops}>
                {template}
            </div>
    )
}

export default Selection;
