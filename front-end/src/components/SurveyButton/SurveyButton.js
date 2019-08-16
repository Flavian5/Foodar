import React from 'react';

const SurveyButton = (props) => {
    return (
        <div onClick={props.onClick} className="survey-btn">
            {props.title}
        </div>
    );
};

export default SurveyButton;