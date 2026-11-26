import urllib.request
import GEOparse
from pathlib import Path

def data_download(cache, output):

    gse_ids = ["GSE73661", "GSE23597", "GSE16879", "GSE52746"]

    cache_dir = Path(cache)
    out_dir = Path(output)
    cache_dir.mkdir(parents=True, exist_ok=True)
    out_dir.mkdir(parents=True, exist_ok=True)

    for gse_id in gse_ids:
        soft_path = cache_dir / f"{gse_id}_family.soft.gz"
        
        # 1. Download directly via HTTPS if not already cached
        if not soft_path.exists():
            prefix = gse_id[:-3] + "nnn"
            url = f"https://ftp.ncbi.nlm.nih.gov/geo/series/{prefix}/{gse_id}/soft/{gse_id}_family.soft.gz"
            print(f"Downloading {gse_id}...")
            urllib.request.urlretrieve(url, soft_path)
        
        # 2. Parse the local file with GEOparse
        print(f"Parsing {gse_id}...")
        gse = GEOparse.get_GEO(filepath=str(soft_path), silent=True)
        
        # 3. Save expression matrix (samples x probes) and metadata
        expr_df = gse.pivot_samples("VALUE").T
        expr_df.to_csv(out_dir / f"{gse_id}_expression.csv")
        
        meta_df = gse.phenotype_data
        meta_df.to_csv(out_dir / f"{gse_id}_metadata.csv")
        
        print(f"  Saved {gse_id}: {expr_df.shape[0]} samples x {expr_df.shape[1]} probes")

    print("Done!")