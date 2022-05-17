// Input Supporting Text, Email, Password

import React from 'react'

const supported = ['text','email','password']

const Input = (props) => {

    const {type, inputHandler, name, ...rest} = props;

    // console.log(props)

    let template;

    if(!supported.includes(type)){
        template = <input className="form-control" type="text" placeholder="-----" readOnly id={`${name}_input`}/>
    }


    template = <input type={type} name={name} onChange={inputHandler} className="form-control" id={`${name}_input`}/>

    return (
    <div>
        {template}
        {/* <label htmlFor={`${name}_input`}>Email address</label> */}
    </div>)
}

export default Input
