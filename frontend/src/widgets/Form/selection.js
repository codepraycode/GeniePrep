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
                <div className="form-check form-check-inline" key={i}>
                    <input 
                        type={type} 
                        name={name} 
                        id={`${option}_option`}
                        onChange={inputHandler}
                        className="form-check-input"
                    />

                    <label 
                        htmlFor={`${option}_option`} 
                        className="form-check-label"
                    >
                        <span>{option}</span>
                    </label>
                </div>
                
            )
        }
    
    )

    return (
        <div className="form_selection">
            {template}
        </div>
    )
}

export default Selection;
