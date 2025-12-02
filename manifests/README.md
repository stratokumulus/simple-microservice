# Workflow 

## Install ArgoCD
Namespace: argocd
If needed, download the manifest and make sure the argocd-server service uses LoadBalancer (not needed, but so much easier)

Get the admin password with the command 
```bash

kubectl -n argocd get secret argocd-initial-admin-secret -o jsonpath="{.data.password}" | base64 -d; echo
```

## Install ArgoCD rollouts
Namespace: argo-rollouts
Only needed for blue-green and canary

# Install the ArgoCD rollouts plugin 
Remove the -linux-amd64 or -darwin-amd64

## Deploy Application

Check the status of the rollout: 

```bash
k argo rollouts get rollout micro-rollout -n simple
```

### Blue-Green
For a blue-green strategy, use the preview service to use the new revision
Once happy with the result, promote the new revision 

```bash
k argo rollouts promote micro-rollout -n simple
```
This will move the active service to the new deployment, and delete the previous revision

### Canary
