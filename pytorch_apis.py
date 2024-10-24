import torch as th
import gp_apis

class linear_impl(th.autograd.Function):
    @staticmethod
    def forward(ctx, X, W, dim1_0, dim1_1, device0):
        res = gp_apis.gp_linear(X, W, dim1_0, dim1_1, device0)
        ctx.backward_cache = None #must be implemented
        return res

    @staticmethod
    def backward(ctx, dZ):
        pass #must be implemented

def linear(X, W, dim1_0, dim1_1, device0):
    return linear_impl.apply(X, W, dim1_0, dim1_1, device0)

class gspmmv_impl(th.autograd.Function):
    @staticmethod
    def forward(ctx, graph, input1, dim_0, dim_1, reverse, norm, device0):
        res = gp_apis.gp_gspmmv(graph, input1, dim_0, dim_1, reverse, norm, device0)
        ctx.backward_cache = input1 #must be implemented
        return res

    @staticmethod
    def backward(ctx, dZ):
        input = ctx.backward_cache
        # res = gp_apis.gp_gspmmv(graph, input, dim_0, dim_1, reverse, norm, device0)
        return input*dZ

def gspmmv(graph, input1, dim_0, dim_1, reverse, norm, device0):
    return gspmmv_impl.apply(graph, input1, dim_0, dim_1, reverse, norm, device0)

