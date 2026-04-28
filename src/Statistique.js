import React from 'react';
import './Statistique.css';

// On utilise la déstructuration pour récupérer chiffre et label
function Statistique({ chiffre, label }) {
  return (
    <div className="stat-card">
      <span className="stat-chiffre">{chiffre}</span>
      <span className="stat-label">{label}</span>
    </div>
  );
}

export default Statistique;