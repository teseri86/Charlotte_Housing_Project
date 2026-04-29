from sklearn.model_selection import train_test_split

def get_reg_splits(master_df):
    # Define feature columns (exclude NPA and target variables)
    drop_cols = ["NPA", "housing_cost_burden", "displacement_risk",
                 "race_white",            
                 "financial_proximity",   # redundant with transit and grocery proximity
                 "housing_density"        # redundant with transit proximity
                ]
    feature_cols = [c for c in master_df.columns if c not in drop_cols]
    X = master_df[feature_cols]
    y = master_df["housing_cost_burden"]
    
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=42
    )
    
    return X_train, X_test, y_train, y_test


def get_class_splits(master_df):
    feature_cols = [c for c in master_df.columns if c not in ["NPA", "housing_cost_burden", "displacement_risk"]]
    X = master_df[feature_cols]
    y = master_df["displacement_risk"]
    
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=42, stratify=y
    )
    
    return X_train, X_test, y_train, y_test