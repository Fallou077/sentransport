// StatReseau.js
function StatReseau({ lignes }) {
  // Calculs logiques
  const totalLignes = lignes.length;
  
  // Somme de tous les arrêts (avec .reduce)
  const totalArrets = lignes.reduce((acc, ligne) => acc + ligne.arrets, 0);

  // Trouver la ligne avec le plus d'arrêts
  const ligneMax = lignes.reduce((prev, current) => 
    (prev.arrets > current.arrets) ? prev : current
  );

  return (
    <div className="stat-reseau" style={{ 
        backgroundColor: '#f8f9fa', 
        padding: '15px', 
        borderRadius: '8px', 
        marginBottom: '20px',
        border: '1px solid #dee2e6' 
    }}>
      <h2 style={{ marginTop: 0 }}>Statistiques du Réseau</h2>
      <div style={{ display: 'flex', gap: '20px' }}>
        <p>Lignes : <strong>{totalLignes}</strong></p>
        <p>Total arrêts : <strong>{totalArrets}</strong></p>
        <p>Ligne la plus longue : <strong>{ligneMax.numero}</strong> ({ligneMax.arrets} arrêts)</p>
      </div>
    </div>
  );
}

export default StatReseau;
