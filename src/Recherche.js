import './Recherche.css';

function Recherche({ valeur, onChange }) {
  return (
    <div className="recherche-container" style={{ display: 'flex', gap: '10px', marginBottom: '20px' }}>
      <input
        className="recherche-input"
        type="text"
        placeholder="Rechercher une ligne (ex: 1, Pikine...)"
        value={valeur}
        onChange={(e) => onChange(e.target.value)}
      />
      <button 
        onClick={() => onChange("")}
        style={{ padding: '0 16px', borderRadius: '8px', cursor: 'pointer' }}
      >
        Effacer
      </button>
    </div>
  );
}

export default Recherche;