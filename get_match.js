import { initializeApp } from "firebase/app";
import { getFirestore, collection, getDocs, doc, deleteDoc } from "firebase/firestore";

const firebaseConfig = {
    apiKey: "AIzaSyCAewfOmvGXYXRctwSe3ylWG5FMohGccWk",
    authDomain: "refurbi-33690.firebaseapp.com",
    projectId: "refurbi-33690",
    storageBucket: "refurbi-33690.firebasestorage.app",
    messagingSenderId: "964460492417",
    appId: "1:964460492417:web:12df82471c478219543f80",
    measurementId: "G-4PZKG80N8F"
};

const app = initializeApp(firebaseConfig);
const db = getFirestore(app);

async function run() {
    const snap = await getDocs(collection(db, "octavos"));
    let matchId = null;
    snap.forEach(doc => {
        const data = doc.data();
        if ((data.local === "Argentina" && data.visitante === "Jordan") || (data.local === "Jordan" && data.visitante === "Argentina")) {
            console.log("Found match:", doc.id, data);
            matchId = doc.id;
        }
    });

    if (matchId) {
        const predId = `julian_${matchId}`;
        console.log("Will delete prediction:", predId);
        await deleteDoc(doc(db, "predicciones", predId));
        console.log("Prediction deleted successfully.");
        
        // Also check if 'Julian' with capital J exists, because names are case sensitive
        const predId2 = `Julian_${matchId}`;
        await deleteDoc(doc(db, "predicciones", predId2));
        console.log("Prediction deleted successfully (capital J).");
        
    } else {
        console.log("Match not found");
    }
    process.exit(0);
}

run();
