import React, { Component } from 'react';
import SurveyButton from '../SurveyButton/SurveyButton';
import Stepper from 'react-stepper-horizontal';

class Survey extends Component {
    state = {
        step: 0,
        prefType: "",

    }

    nextStep = () => {
        this.setState({
            step: this.state.step + 1
        })
    }
    goBack = () => {
        this.setState({
            step: this.state.step - 1
        }, () => {
            console.log(this.state)
        })
    }

    selectItem = (item) => {
        console.log(item);
        this.setState({
            step: this.state.step + 1,
            prefType: this.state.step === 1 ? item : this.state.prefType
        })
        
    }
    render() {
        let step0 = {
            title: "What is your Meal Type/Restrictions?",
            options: ["Vegetarian", "Vegan", "Kosher", "Gluten-free"]
        }
        let step1 = {
            title: "What kind of food do you like?",
            options: ["American", "European", "Middle Eastern", "Asian"] 
        }

        let AmericanStep = {
            title: "What type of American Food do you like?",
            options: ["Burgers", "Pub", "Wings", "Tacos", "Burrito"]
        }

        let EuropeanStep = {
            title: "What type of European food do you like?",
            options: ["Italian", "French", "German/Austrian", "Spanish"]
        }

        let MiddleEasternStep = {
            title: "What type of Middle Eastern food do you like?",
            options: ["Hummus", "Falafel", "Tabouleh", "Fattoush", "Shawarma", "Kebab"]
        }

        let AsianFoodStep = {
            title: "What type of Asian food do you like?",
            options: ["Japanese", "Chinese", "Thai", "Indian", "Korean"]
        }

        let step3 = {
            title: "How much do you want to spend?",
            options: ["$", "$$", "$$$"]
        }

        let step4 = {
            title: "Dine-in or Takeout?",
            options: ["Dine-in", "Takeout"]
        }

        let foodType = {
            "American": AmericanStep,
            "European": EuropeanStep,
            "Middle Eastern": MiddleEasternStep,
            "Asian": AsianFoodStep
        }

        let getStep = () => {
            let step = this.state.step;
            if(step === 0) {
                return step0;
            }
            if(step === 1) {
                return step1;
            }
            if(step === 2) {
                return foodType[this.state.prefType]
            }
            if(step === 3) {
                return step3
            }
            return step4;
        }



        let step = getStep();
        return (
            <div className="survey-menu" style={{borderRadius: 5, padding: '15px 20px', backgroundColor: 'white', paddingBottom: 25}}>
                <Stepper completeColor={"#EAA55C"} activeColor={"#8D8276"} activeTitleColor={"#8B8072"} titleFontSize={12} steps={ [{title: 'Step One'}, {title: 'Step Two'}, {title: 'Step Three'}, {title: 'Step Four'}] } activeStep={ this.state.step } />
                <p style={{fontSize: 30, fontWeight: 500, color: '#8D8276', textAlign: 'center'}}>{step.title}</p>
                <div style={{ display: 'flex', flexWrap: 'wrap', paddingLeft: 50, paddingRight: 50, justifyContent: 'center', maxHeight: 220, overflow: 'auto'}}>
                        {
                            step.options.map((item, i) => <div style={{margin: '20px 15px'}}><SurveyButton onClick={() => this.selectItem(item)} title={item}/></div>)
                        }
                </div>
                <div style={{position: 'relative', marginTop: 20, height: 50}}>
                    {this.state.step > 0 && <button onClick={this.goBack} className="foodar-btn-2">Back</button>}
                    {/* <button onClick={this.nextStep} style={{position: 'absolute', right: 0}} className="foodar-btn-2">Next</button> */}
                </div>
            </div>
        );
    }
}

export default Survey;