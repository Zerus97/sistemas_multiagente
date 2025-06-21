import pandas as pd

base_line = (0.55 + 0.66 + 0.48 + 0.72 + 0.96 + 0.71 + 0.77 + 0.84 + 0.85 + 0.91 + 0.91 + 0.95) / 12

df_egoista = pd.read_csv("resultados_com_egoista/game_results_different_story_ag4_ro5_end10_mult1.5.csv")
df_egoista_collab_score = df_egoista.query('PromptType == "All"')[["CollaborationScore"]]
egoista_collab_score_mean = (df_egoista_collab_score.mean()).iloc[0]

df_colaborador = pd.read_csv("resultados_sem_egoista/game_results_different_story_ag4_ro5_end10_mult1.5.csv")
df_colaborador_collab_score = df_colaborador.query('PromptType == "All"')[["CollaborationScore"]]
colaborador_collab_score_mean = (df_colaborador_collab_score.mean()).iloc[0]

comparativo_egoista = ((egoista_collab_score_mean / base_line) - 1) * 100

comparativo_colaborador = ((colaborador_collab_score_mean / base_line) - 1) * 100

print(f"""
==== Resultados ====
Baseline Collaboration Score: {base_line:.4f}

Egoísta Collaboration Score: {egoista_collab_score_mean:.4f}
Diferença em relação ao baseline: {comparativo_egoista:.2f}%

Colaborador Collaboration Score: {colaborador_collab_score_mean:.4f}
Diferença em relação ao baseline: {comparativo_colaborador:.2f}%
""")