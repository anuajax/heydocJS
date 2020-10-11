const mongoose = require("mongoose");
const Treatment = new mongoose.Schema({
    patient_name: {type: String, required:true},
    disease: {type: String, required: true},
    doctor_name: {type:String,required:true},
    prescription_files: WeavyFileSystem 
})
const PatientModel = new mongoose.Schema({
 name: { type: String, required: true},
 email: { type: String, required: true},
 username: { type: String, unique: true, required: true},
 password: { type: String, required: true},
 profileImage: {type:Image},
 contact: {type:String,required: true},
 //above to be filled during Signup/ 
 comingAppontmentwithDoctors: WeavyTODOList,
 onGoingTreatments: [Treatment],
notifications: WeavyNotifications,
chats: From-Weavy
});

module.exports = mongoose.model("PatientSchema",PatientModel)