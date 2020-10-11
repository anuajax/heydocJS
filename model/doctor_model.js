const mongoose = require("mongoose");
const AppointmentSchema = new mongoose.Schema({
    patient_name: {type: String, required:true},
    disease: {type: String, required: true},
    doctor_name: {type:String,required:true},
    //above to be filled by patient while posting a request below to be done by doctor while accepting
    approved: {type: Boolean, default:false},
    date: {type:Date, default:null},
    prescription_files: {type: WeavyFileSystem}

})
const DoctorModel = new mongoose.Schema({
 name: { type: String, required: true},
 email: { type: String, required: true},
 username: { type: String, unique: true, required: true},
 password: { type: String, required: true},
 degrees: { type: String, required: true},
 specialist_of: { type: String, required: true},
 profileImage: {type:Image},
 addresses_clinics: [ {location:String,clinicPhoneNo: String} ],
 contact_phone: {type:String,required:true},
 //above stuffs will be asked in SignUp form
 
 comingAppointments:  WeavyTODOList,
 new_or_pendingAppointments: [AppointmentSchema],
 currentPatients: [ { type: mongoose.Schema.Types.ObjectId, ref: "PatientSchema"} ],
 notifications: WeavyNotifications,
 chats: From-Weavy
});

module.exports = mongoose.model("DoctorSchema",DoctorModel)