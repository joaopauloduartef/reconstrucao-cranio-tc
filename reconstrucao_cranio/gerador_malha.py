import plotly.graph_objects as go
from skimage import measure

class GeradorMalha:
    @staticmethod
    def plotar_volume_3d(volume, limiar_osso, fator_z_real):
        print("\n-> Extraindo a malha 3D com o algoritmo Marching Cubes...")
        # Extrai os vértices e as faces da isosuperfície
        verts, faces, normals, values = measure.marching_cubes(volume, limiar_osso, step_size=1)
        
        print("-> Renderizando o modelo 3D com Plotly...")
        # Separa as coordenadas x, y, z dos vértices
        x, y, z = verts.T
        
        # Aplica o fator de correção no eixo Z para garantir a proporção anatômica real
        z = z * fator_z_real
        
        # Separa as conexões dos triângulos (faces)
        i, j, k = faces.T
        
        # Cria a figura 3D interativa
        fig = go.Figure(data=[go.Mesh3d(
            x=x, y=y, z=z,
            i=i, j=j, k=k,
            color='lightgray',
            opacity=0.7,
            lighting=dict(ambient=0.4, diffuse=0.6, roughness=0.9, specular=0.5, fresnel=0.2)
        )])
        
        fig.update_layout(
            title="Reconstrução 3D do Crânio",
            scene=dict(
                xaxis=dict(showbackground=False, visible=False),
                yaxis=dict(showbackground=False, visible=False),
                zaxis=dict(showbackground=False, visible=False),
                aspectmode='data' # Mantém as proporções reais
            ),
            margin=dict(l=0, r=0, b=0, t=50)
        )
        
        fig.show()